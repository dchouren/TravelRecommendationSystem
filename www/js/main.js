
angular.module('travelRecommender', [])
  .controller('travelController', ['$scope', function($scope) {
    $scope.cities = [
      {text:'Te Anau, New Zealand', toRemove:true, lineBreak:0},
      {text:'Paphos, Cyprus', toRemove:false, lineBreak:0},
      {text:'Istanbul, Turkey', toRemove:true, lineBreak:0},
      {text:'Denali National Park and Preserve, AK, USA', toRemove:false, lineBreak:1},
      {text:'New York City, NY, USA', toRemove:true, lineBreak:0},
      {text:'Ibiza, Spain', toRemove:false, lineBreak:1},
      {text:'Paris, France', toRemove:true, lineBreak:0},
      {text:'Jasper National Park, Alberta, Canada', toRemove:false, lineBreak:0},
      {text:'Hong Kong, China', toRemove:true, lineBreak:1},
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
      if ($scope.cityText.length != 0) {
        $scope.cities.push({text:$scope.cityText, toRemove:false});
        $scope.cityText = '';
      }
      $scope.toggleLineBreak();
    };

    $scope.deleteCity = function(index) {
      $scope.cities.splice(index, 1);
      $scope.toggleLineBreak();
    }

    $scope.remaining = function() {
      var count = 0;
      angular.forEach($scope.cities, function(city) {
        count += city.done ? 0 : 1;
      });
      return count;
    };

    $scope.archive = function() {
      var oldCities = $scope.cities;
      $scope.cities = [];
      angular.forEach(oldCity, function(city) {
        if (!city.toRemove) $scope.cities.push(city);
      });
    };

  }]);

