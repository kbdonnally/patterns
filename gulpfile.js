// requirements:
var gulp 		 = require('gulp');

// plugins:
var autoprefixer = require('gulp-autoprefixer'),
	concat 		 = require('gulp-concat'),
	csso 		 = require('gulp-csso'),
	htmlmin 	 = require('gulp-htmlmin'),
	sass 		 = require('gulp-sass'),
	uglify 		 = require('gulp-uglify'); 

// tasks:

var src_js = './assets/js-new/_js/*.js';
var dest_js = './assets/js-new';



