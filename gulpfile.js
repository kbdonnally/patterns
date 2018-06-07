// requirements:
var gulp 		 = require('gulp');

// plugins:
var autoprefixer = require('gulp-autoprefixer'),
	clean		 = require('gulp-clean'),
	concat 		 = require('gulp-concat'),
	csso 		 = require('gulp-csso'),
	htmlmin 	 = require('gulp-htmlmin'),
	sass 		 = require('gulp-sass'),
	uglify 		 = require('gulp-uglify'); 

// tasks:

var src_js = './assets/js-new/_js/*.js';
var dest_js = './assets/js-new';

var format_js = () => {
	return gulp.src(src_js)
		.pipe(concat('main.js'))
		.pipe(uglify({mangle:false}))
		.pipe(gulp.dest(dest_js));
};

gulp.task('watch_js', () => {
	return gulp.watch(src_js, format_js);
});
