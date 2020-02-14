$(document).ready(function () {
  $.getJSON('https://swapi.co/api/films/?format=json', function (result) {
    for (const movie of result.results) {
      $('ul#list_movies').append("<li>" + movie.title + "</li>");
    }
  });
});
