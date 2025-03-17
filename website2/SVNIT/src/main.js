import $ from 'jQuery'

$(document).ready(function() {
  let index = 0;
  const totalSlides = $(".carousel img").length;
  
  function showSlide() {
      $(".carousel").css("transform", `translateX(-${index * 100}%)`);
  }
  
  $(".next").click(function() {
      index = (index + 1) % totalSlides;
      showSlide();
  });
  
  $(".prev").click(function() {
      index = (index - 1 + totalSlides) % totalSlides;
      showSlide();
  });
  
  setInterval(function() {
      index = (index + 1) % totalSlides;
      showSlide();
  }, 4200);
});