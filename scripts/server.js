if (Meteor.isServer) {
	Meteor.call("deleteAllMovies");
	if (Meteor.call("initVar") == false){
		Meteor.call("fileInit");
	}
}
