import os, glob
import logging
from django.http import Http404
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
#from django.contrib.staticfiles.views import serve
from django.views import static
from accounts.models import CustomuserUserWhiteList


logger = logging.getLogger("console")
@login_required
def serve_docs(request, path):
    if not request.user.is_authenticated:
        logger.info("Login required")
        return redirect('/accounts/login/')
    logger.debug("doc_dir: %s", settings.DOCS_DIR)
    document_root = os.path.join(settings.DOCS_BASE_DIR, settings.DOCS_DIR)
    document_root = os.path.join(document_root, path)
    fname=''
    #docs_path = os.path.join(settings.DOCS_DIR, path)
    if os.path.isdir(document_root):
        fname='index.html'
        logger.debug("doc root exist %s"%document_root)
    else:
        if os.path.isfile(document_root):
            document_root, fname = os.path.split(document_root)
        else:
            logger.warning("file could not found: %s"%path)
            document_root = os.path.join(settings.DOCS_BASE_DIR, settings.DOCS_DIR)
            fname = '404.html'
    logger.debug("document_root %s"%document_root)
    """"
    Check permission here
    request.user.department, request.user.division_code, request.user.team_code, request.user.mobile_phone
    """
    #if not request.user.department:
    #   return redirect('/accounts/logout/')
    nav = path.split('/')[0]

    if not get_permission(request.user, nav):
        raise PermissionDenied("You do not have permission to access the documents")
    try:
        return static.serve(request, fname, document_root=document_root)
    except Exception as e:
         logger.error(str(e))
         logger.warning("path %s"%path)
         logger.warning("document_root %s"%document_root)
         logger.warning("document_root %s"%fname)

"""
True: has permission
False: hasn't permission
"""
def get_permission(user_obj, nav):
    if nav == "staff-only":
        try:
            CustomuserUserWhiteList.objects.get(customuser=user_obj)
        except CustomuserUserWhiteList.DoesNotExist:
            logger.debug("You are in %s department"%str(user_obj.department))
            if user_obj.department not in ["GT", "GIO"]:
                logger.warning("%s member of %s hasn't permission accses to staff-only"%(user_obj.username, str(user_obj.department)))
                return False
            else:
                return True
        except Exception as e:
            logger.error(e)
            return False
        else:
            logger.info("%s in white list"%user_obj.username)
            return True
    else:
        return True
 
