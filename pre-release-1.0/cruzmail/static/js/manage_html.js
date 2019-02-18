var myModel = {
    name: "Ashley",
    test: 'asd',
    loading: 24,
    Info: [ {a:1111111, b:"Michael", c:"Mora"},
 	    {a:2222222, b:"Chris"  , c:"UCSC"},
            {a:3333333, b:"Samir"  , c:"SC"},
            {a:4444444, b:"Kevin"  , c:"SC"},
    	    {a:5555555, b:"Sean"   , c:"SC"}],
    name2: "asdadsf",
};

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
var myViewModel = new Vue({
    el: '#my_view',
    delimiters:['${', '}'],
    data: myModel,
    
    methods: {
	sort: sorts = function(){
	    console.log(myViewModel.test);

	},
	newPackage: newPackages = function(){
	    $.ajax({ type: "POST",
		     url:  '' ,
		     data:{}, 
		     success: function good(response){
		         console.log(response);
		     },
		     error: function(response){
			 console.log("ded\n");
		     }
	    });
	}

    }
    
});
