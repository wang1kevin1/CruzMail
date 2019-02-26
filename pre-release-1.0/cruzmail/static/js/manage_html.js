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

var myViewModel = new Vue({
    el: '#my_view',
    delimiters:['${', '}'],
    data: myModel,
    
    methods: {
	sort: sorts = function(){
	     console.log(myViewModel.test);

	}

    }
    
});
