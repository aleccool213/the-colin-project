Router.route('/', function () {
  this.render('colinproject');
});

Router.route('/thelegend/', function () {
  this.render('about');
});

Router.route('/television/', function () {
  this.render('television');
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
  this.layout('showTitle',{
    data: {
      title: film.title,
      posterLocation: film.location
    }
  });

});