console.log('Hi, there the JS file is working');

$('img.image').error(function () {
    console.log(this);
    $(this).remove();
});