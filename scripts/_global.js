Router.route('/', function () {
  this.render('colinproject');
});

Router.route('/thelegend/', function () {
  this.render('about');
});

Router.route('/film/', function () {
  this.render('film');
});


Movies = new Mongo.Collection("movies");
Movies.initEasySearch('title');


if (Meteor.isClient) {

  Template.cont.helpers({
    movies: function () {
      return Movies.find({});
    }

  });
    
  
}

Router.route('/film/show/:title', function () {
  var film = Movies.findOne({title: this.params.title});
  this.layout('showFilm',{
    data: {
      title: film.title,
      posterLocation: film.location
    }
  });

});