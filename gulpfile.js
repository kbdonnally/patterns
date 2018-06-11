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

// js:

// set file locations
var src_js = './assets/js-new/_js/*.js';
var dest_js = './assets/js-new';

// minify & combine files
var format_js = () => {
	return gulp.src(src_js)
		.pipe(concat('main.js'))
		.pipe(uglify({mangle:false}))
		.pipe(gulp.dest(dest_js));
};

gulp.task('watch_js', () => {
	return gulp.watch(src_js, format_js);
});

gulp.task('clean_js', () => {
	return gulp.src('assets/js-new/main.js', { allowEmpty: true })
		.pipe(clean());
});

gulp.task('js', gulp.series('clean_js', 'watch_js'));

// css:


var format_css = () => {
	return gulp.src('_site/assets/css/style.css')
		.pipe(autoprefixer({
			browsers: ['last 2 versions'],
			grid: true
		}))
		.pipe(gulp.dest('testing/gulp-output/css'));
};

gulp.task('watch_css', () => {
	return gulp.watch('_site/assets/css/style.css', format_css);
});