

myApp = angular.module('myApp.directives', []);




myApp.directive('addClass', function(){
    return{
        restrict: 'A',
        templateUrl : '/add_class_template',
        transclude : true
    };
});

