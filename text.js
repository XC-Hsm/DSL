test()
async function test() {
    $("textToSend").value="测试";
    $("sendinput").click();
    await sleep(2000);
    $("textToSend").value="测试";
    $("sendinput").click();
    await sleep(2000);
    $("textToSend").value="测试";
    $("sendinput").click();
    await sleep(2000);
}