
var Post = Backbone.Model.extend({
	urlRoot: 'http://0.0.0.0:8080/post/',
	defaults: {
		body: ""
	}
});

function post_reg() {
	var newBody = document.getElementById("form_mail").value;

	var newPost = new Post({
		body: newBody
	});
alert(JSON.stringify(newPost));
newPost.save();
};
