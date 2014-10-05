var js = document.createElement("script");

js.type = "text/javascript";
js.src = "static/js/helper.js";

var travelRecommender = angular.module('travelRecommender', []);

travelRecommender.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

travelRecommender.controller('travelController',
  ['$scope', '$http', '$location', function($scope, $http, $location) {
    $scope.cities = [
      {text:'Te Anau, New Zealand', toRemove:false, lineBreak:0},
      {text:'Paphos, Cyprus', toRemove:false, lineBreak:0},
      {text:'Istanbul, Turkey', toRemove:false, lineBreak:0},
      {text:'Denali National Park and Preserve, AK, USA', toRemove:false, lineBreak:1},
      {text:'New York City, NY, USA', toRemove:false, lineBreak:0},
      {text:'Ibiza, Spain', toRemove:false, lineBreak:1},
      {text:'Paris, France', toRemove:false, lineBreak:0},
      {text:'Jasper National Park, Alberta, Canada', toRemove:false, lineBreak:0},
      {text:'Hong Kong, China', toRemove:false, lineBreak:1},
      {text:'Prague, Czech Republic', toRemove:false, lineBreak:0}
    ];


    $scope.columns = $scope.cities.length / 5;

    $scope.toggleLineBreak = function() {
      var charCounter = 0;
      angular.forEach($scope.cities, function(city) {
        charCounter += city.text.length;
        city.lineBreak = 0;
        if (charCounter > 80) {
          city.lineBreak = 1;
          charCounter = city.text.length;
        }
      })
    };

    $scope.addCity = function() {
      // check if location already added
      $scope.duplicate = 0;
      for (var i = 0; i < $scope.cities.length; i++) {
        if ($scope.cities[i].text == $scope.cityText) {
          focusSearch();
          $scope.cityText = '';
          $scope.duplicate = 1;
          return;
        }
      }
      if ($scope.cityText) {
        $scope.cities.push({text:$scope.cityText, toRemove:false});
        $scope.cityText = '';

        $scope.toggleLineBreak();


        $scope.recommendations = [];
        console.log("add " + $scope.recommendations.length);
      }

      focusSearch();
    };

    $scope.deleteCity = function(index) {
      $scope.cities.splice(index, 1);
      $scope.toggleLineBreak();

      $scope.recommendations = [];
      console.log("delete " + $scope.recommendations.length);

      focusSearch();
    }

    $scope.deleteRec = function(index) {
      $scope.recommendations.splice(index, 1);

      console.log("delete " + $scope.recommendations.length);

      focusSearch();
    }

    $scope.remaining = function() {
      var count = 0;
      angular.forEach($scope.cities, function(city) {
        count += city.done ? 0 : 1;
      });
      return count;
    };

    $scope.clear = function() {
      $scope.cities = [];

      $scope.recommendations = [];
      console.log("clear " + $scope.recommendations.length);

      focusSearch();
    };

    $scope.recommend = function() {

      $scope.recommending = 1;

      var citiesQuery = $scope.cities;

      // console.log(JSON.stringify(citiesQuery));

      // $http
      $http({
        url: 'recommend',
        method: 'POST',
        data: citiesQuery,
        dataType: 'JSON'
      }).success(function(data) {
        // console.log(data);
        console.log('success');

        $scope.recommendations = data;

        console.log("recommend " + $scope.recommendations.length);

        // focusSearch();
        $scope.recommending = 0;

      }).error(function() {
        console.log('error');
        $scope.recommending = 0;
      });

    }

  }]);



