'use strict';

/**
 * @ngdoc function
 * @name ngntsApp.controller:ScopedetailCtrl
 * @description
 * # ScopedetailCtrl
 * Controller of the ngntsApp
 */
angular.module('ngntsApp')
  .controller('ScopeDetailCtrl', function ($scope, $routeParams) {
    $scope.scope = decodeURIComponent($routeParams.scope);
  });
