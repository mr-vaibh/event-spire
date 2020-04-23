console.log('Hi, there the JS file is working');

$('img').error(function () {
    console.log(this);
    $(this).remove();
});