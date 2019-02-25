var myModel = {
    name: "Ashley",
    test: 'asdsa', 
    new_mailstop: '',
    new_route: '',
    index: 0,
    
    new_tracknum: '',
    new_name: '',
    new_sign: '',
    new_email: '',
    new_remark: '',
    Info: [],
};

var myViewModel = new Vue({
    el: '#my_view',
    delimiters:['${', '}'],
    data: myModel,
    
    methods: {
	addPackage: addPackages = function(){
	    $.ajax({ type: "POST",
                     url:  '/add_package' ,
                     data:{"track":    myViewModel.new_tracknum,
			   "name":     myViewModel.new_name,
			   "mailstop": myViewModel.new_mailstop,
		           "sign":     myViewModel.new_sign,
		           "email":    myViewModel.new_email,
		           "remark":   myViewModel.new_remark},
                     dataType: 'json',
                     success: function no(response){
                     },
                     error: function(response){
                         console.log("invalid inputs\n");
                     }
            });

	},
	updatePackage: updatePackages = function(){
	    $.ajax({ type: "POST",
                     url:  '/query_package' ,
                     data:{
                           "index": myViewModel.index * 10},
                     dataType: 'json',
                     success: function no(response){
                     },
                     error: function(response){
                         console.log("invalid inputs\n");
                     }
            });

	},
	packageDelivered: packagesDelivered = function(){
	    $.ajax({ type: "POST",
                     url:  '/query_package' ,
                     data:{
                           "index": myViewModel.index * 10},
                     dataType: 'json',
                     success: function no(response){
                     },
                     error: function(response){
                         console.log("invalid inputs\n");
                     }
            });

	},
	queryPackage: queryPackages = function(){
	    //end function if user tried to press previous page while page was 0
	    if(myViewModel.index < 0){
		myViewModel.index = 0;
		return;
	    }
	    $.ajax({ type: "POST",
		     url:  '/query_package' ,
		     data:{
		           "index": myViewModel.index * 10}, 
		     dataType: 'json',
		     success: function good(response){
			 myViewModel.Info = [];
		         for(var key in response.params){
				myViewModel.Info.push({a:response.params[key].a,
						       b:response.params[key].b,
						       c:response.params[key].c,
						       d:false});
				//console.log(response.params[key]);
			 }
		     },
		     error: function(response){
			 console.log("invalid inputs\n");
		     }
	    });
	}

    }
    
});
myViewModel.queryPackage();
