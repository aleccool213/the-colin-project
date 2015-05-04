
Movies = new Mongo.Collection("movies");
Movies.initEasySearch('title');

Meteor.methods({
  /*
  Method to run on the server at startup to see if fileinit has run yet or not. 
  AKA No migrations in Meteor so just making this to mock one.
  */
  initVar: function(){
    if (Movies.find({}).fetch().length == 0){
      return false
    }
    else{
      return true
    }
  },
  /*
  Method to run on the server if initVar returns False at startup to fill in the db with titles 
  from the tweet archive (public/datafiles/resultsComplete.txt) 
  */
  fileInit: function(){
    
    var Fiber = Npm.require('fibers')
    var fs = Npm.require("fs");
    var readline = Npm.require('readline');
    //var files = fs.readdirSync('/assets');

    //get path to private
    var meteor_root = fs.realpathSync(process.cwd() + '/../');
    var application_root = fs.realpathSync(meteor_root + '/../');
    var assets_folder = meteor_root + '/server/assets/app';

    //Read every line of the movie list
    var rd = readline.createInterface({
        input: fs.createReadStream(assets_folder + '/datafiles/resultsComplete.txt'),
        output: process.stdout
    });

    //for every line, insert the title and list of seasons in the db via an async call
    rd.on('line', function(line) {
      Fiber(function(){
        //get the title, chars up to the `:`
        titleIndex = line.indexOf(':');
        titleString = line.substring(0 , titleIndex);
        console.log(titleString);
        //get the seasons 
        seasonsList = line.substring((titleIndex + 3),(line.length - 1));
        //console.log(seasonsList);
        var array = JSON.parse("[" + seasonsList + "]");
        console.log(array)
        Meteor.call("addMovie", titleString, array);
      }).run();
    });
  },

  addMovie: function (title, seasons) {
    var data = Meteor.call("findMovieData", title)
    Movies.insert({
      title: title,
      seasons: seasons,
      banner_location: data["Poster"],
      year: data["Year"],
      rating: data["Rated"],
      released: data["Released"],
      genre: data["Genre"],
      plot: data["Plot"],
      awards: data["Awards"],
      createdAt: new Date()
    });
  },
 
  deleteMovie: function (movieId) {
    Movies.remove(movieId);
  },
  //used for testing purposes
  deleteAllMovies: function(){
    Movies.remove({});
  },
  
  //Api request to get data
  findMovieData: function(title){
    this.unblock();
    movieJSON = Meteor.http.call("GET", "http://www.omdbapi.com/?t=" + title + "&y=&plot=short&r=json");
    data = JSON.parse(movieJSON.content)
    return data;
  },


});