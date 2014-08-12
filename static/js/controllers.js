var wantedApp = angular.module('WantedApp', []);

wantedApp.controller('WantedController', ['$scope', '$http', function($scope, $http) {
    $http.get('/wanteddata').success(function(data) {
        $scope.files = data;
        $scope.fileOrder = 'surname';
    });
}]);
