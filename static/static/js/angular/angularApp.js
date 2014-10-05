var js = document.createElement("script");

js.type = "text/javascript";
js.src = "static/js/helper.js";

var travelRecommender = angular.module('travelRecommender', []);

travelRecommender.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);