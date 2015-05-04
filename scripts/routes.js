
Router.route('/', function () {
  this.render('colinproject');
});

Router.route('/thelegend/', function () {
  this.render('about');
});

Router.route('/television/', function () {
  this.render('television');
});

Router.route('/film/show/:title', function () {
  var film = Movies.findOne({title: this.params.title});
  this.layout('showTitle',{
    data: {
      title: film.title,
      posterLocation: film.banner_location,
      year: film.year,
      rating: film.rating,
      released: film.released,
      genre: film.genre,
      plot: film.plot,
      colins_thoughts: "*COLINS THOUGHTS HERE*",
      awards: film.awards,
      seasons: film.seasons
    }
  });

});