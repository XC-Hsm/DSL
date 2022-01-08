function $(id) { return $(id); }
function initzx() {
    document.getElementsByClassName("chatBox-head-one")[0].style.display = 'none';
    document.getElementsByClassName("chatBox-list")[0].style.display = 'none';
    $("chatBoxkuang").style.display = 'inline-flex';
    $("chatBoxkuang").style.width = "80%";
    $("chatSend").style.width = "80%";
    $("rightinfo").style.display = 'block';
    document.getElementsByClassName("chatBox-head-two")[0].style.display = 'inline-flex';
}
function returnList() {
    document.getElementsByClassName("chatBox-list")[0].style.display = 'block';
    $("chatBoxkuang").style.display = 'none';
    $("chatBoxkuang").style.width = "100%";
    $("chatSend").style.width = "100%";
    $("rightinfo").style.display = 'none';
    document.getElementsByClassName("chatBox-head-one")[0].style.display = 'block';
    document.getElementsByClassName("chatBox-head-two")[0].style.display = 'none';
}

function sleep(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}
