'use strict';

/**
 * @ngdoc function
 * @name ngntsApp.controller:ScopelistCtrl
 * @description
 * # ScopelistCtrl
 * Controller of the ngntsApp
 */
angular.module('ngntsApp')
  .controller('ScopeListCtrl', function ($scope) {
    var minFont = 12.0,
        maxFont = 36.0,
        diffFont = maxFont - minFont;


    var words = [];
    for(var x in $scope.idx.scopes){
        var size = (Math.log($scope.idx.scopes[x]['count']));// / Math.log({{ max }})) * diffFont + minFont;
        words.push({text:x, weight:size, link:'#/scopes/'+x});
    };

    $scope.words = words;
     // $scope.words = [
        // {text: "Lorem", weight: 13, link: 'http://github.com/mistic100/jQCloud'},
        // {text: "Ipsum", weight: 10.5},
        // {text: "Dolor", weight: 9.4},
        // {text: "Sit", weight: 8},
        // {text: "Amet", weight: 6.2},
        // {text: "Consectetur", weight: 5},
        // {text: "Adipiscing", weight: 5},
     // ];


    // $timeout(angular.noop, 2000)
    //     .then(function(){
    //         $scope.tags = [
    //             {text:'aaaaa', value: 35},
    //             {text:'bbb', value: 5},
    //             {text:'cc', value: 6},
    //             {text:'ddd', value: 8},
    //             {text:'e', value: 15},
    //             {text:'aaafaa', value: 25}
    //         ];

    //         $interval(function(){
    //             if ($scope.liveReloading){
    //                 angular.forEach($scope.tags, fu)
    //             }
    //         })
    //     })
  });
