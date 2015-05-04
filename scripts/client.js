
if (Meteor.isClient) {

  Template.cont.helpers({
    movies: function () {
      return Movies.find({});
    }
  });
    
}