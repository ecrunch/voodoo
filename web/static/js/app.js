

angular.module('myApp', [ 
    'myApp.controllers',
    'myApp.services',
    'myApp.directives',
    'ngRoute'
])
.config(['$routeProvider', function($routeProvider){

    $routeProvider
    .when('/', {
        templateUrl: 'static/partials/home.html',
        controller: 'homeCtrl'
    })
    .when('/schedule', {
        templateUrl: 'static/partials/schedule.html',
        controller: 'scheduleCtrl'
    })
    .when('/add_class', {
        templateUrl: 'static/partials/add_class.html',
        controller: 'addClassCtrl'
    })
    .otherwise({
        redirectTo: '/'
    });

}]);

