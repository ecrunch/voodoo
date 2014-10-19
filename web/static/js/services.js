

myApp = angular.module('myApp.services', []);

//www.sitepoint.com/implementing-authentication-angular-applications/

myApp.factory('authService', function($http, $q, $window){

    var userInfo;

    function login(userName, password){

        var deferred = $q.defer();
        var route = "/login";
    
        $http.post(route).then(
            function(res){
                userInfo= {

                };
                $window.sessionStorage["userInfo"] = JSON.stringify(userInfo);
                deferred.resolve(userInfo);
            },
            function(error){
                deferred.reject(error);
            }
        );

    }

    return {
        login: login
    };

});



