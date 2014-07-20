var ufApp = angular.module('ufApp', []);

ufApp.controller('UfController', ['$scope', '$http', function($scope, $http) {
    $http.get('/ufdata').success(function(data) {
        $scope.files = data;
        $scope.fileOrder = 'surname';
    });
}]);
