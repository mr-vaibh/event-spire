console.log('Hi, there the JS file is working');

$('img.image').on('error', function () {
    console.log(this);
    $(this).remove();
});