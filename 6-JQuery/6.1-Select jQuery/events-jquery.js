// document.selectQuery('h1').addEvenetListener('click',function functionName() {...})
//
// Printohet ne console nje mesazh sa here qe shtyp nje h1 ose nje liste
// $('h1').click(function () {
//   console.log("There was a click!");
// })
//
// $('li').click(function () {
//   console.log('Nje nga lista eshte klikuar!')
// })

// Ndryshohet mszh sa here qe shtypet nje h1 ose nje liste
// $('h1').click(function () {
//   $(this).text('Une jam ndryshuar')
// })


// KEY PRESS
// $('input').eq(0).keypress(function () {
//   $('h2').toggleClass('turnBlue');
// })

// $('input').eq(0).keypress(function (event) {
//   console.log(event);
// })

// $('input').eq(0).keypress(function (event) {
//   if (event.which === 13) {
//     $('h2').toggleClass('turnRed');
//   }
// })


// //on()
// $('h1').on('dblclick',function () {
//   $(this).toggleClass('turnRed');
// })

// KUR MAUSI ESHTE SIPER
// $('h1').on('mouseenter',function () {
//   $(this).toggleClass('turnRed')
// })

$('button').on('click',function () {
  $('.container').fadeOut(3000);
})
$('button').on('dblclick',function () {
  $('.container').fadeIn(5000);
})
