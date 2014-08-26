

myApp = angular.module("myApp.services", []);



myApp.factory('DbContentsManager', [function(){


}]);




// service to handle the http calls to the back end
// for the scheduler
myApp.factory('ScheduleManager', ['$rootScope', '$http', '$q',  function($rootScope, $http, $q){

    
    var make_route = "/get_schedule/";
    var add_route = "/add_minutes";
    var remove_route = "/reset_minutes";
    

    var service = {

        newSchedule:
            function(hours){
                var route = make_route + hours;
                return $http.get(route);
            },

        
        addTime:
            function(id, time_slot, item_class){
                var parms = {
                    id: id,
                    time_slot: time_slot,
                    item_class: item_class
                };
                return $http.get(add_route, {params : parms});
            },

        resetTime:
            function(id, item_class){
                var parms = {
                    id: id,
                    item_class: item_class
                }
                return $http.get(remove_route, {params : parms});
            }

    } 


    return service;    

}]);



myApp.factory('SelectedItemManager', ['$rootScope', '$http', function($rootScope, $http){


    var selectedItem;

    var service = {
        
        test:
            function(){
                alert("Test");    
            },
            

        formatTask:
            function(item){
                return [ 
                    {"field_name" : "ID", "field_value" : item["id"]},
                    {"field_name" : "Type", "field_value" : item["class"]},
                    {"field_name" : "Score", "field_value" : item["score"]},
                    {"field_name" : "Placement", "field_value" : item["placement"]},
                    {"field_name" : "Due Date", "field_value" : item["due_date"]},
                    {"field_name" : "TS (min)", "field_value" : item["total_minutes"]}
                ];
            },

        formatWant:
            function(item){
                return [
                    {"field_name" : "ID", "field_value" : item["id"]},
                    {"field_name" : "Type", "field_value" : item["class"]},
                    {"field_name" : "Category", "field_value" : item["category"]}
                ];
            },

        formatBreak:
            function(item){
                return [
                    {"field_name" : "ID", "field_value" : item["id"]},
                    {"field_name" : "Type", "field_value" : item["class"]},
                    {"field_name" : "URL", "field_value" : item["url"]}
                ];
            }
            
    };

    return service;
}]);





