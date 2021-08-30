@page {
    size: a4 portrait;
    margin: 25mm 10mm 25mm 10mm;
    counter-increment: page;
    font-family: "Roboto","Helvetica Neue",Helvetica,Arial,sans-serif;
    white-space: pre;
    color: grey;
    @top-left {
        content: '© 2021 SO';
    }
    @top-center {
        content: string(chapter);
    }
    @top-right {
        content: 'Page ' counter(page);
    }
}
