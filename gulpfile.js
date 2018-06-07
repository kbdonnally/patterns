// fetch module
var gulp 	 = require('gulp'),
	concat 	 = require('gulp-concat'),
	prefixer = require('gulp-autoprefixer');

// files to read, where to write them
var testFiles = './assets/css/_sass/*.scss',
	outputDir = './testing/gulp-output/concat';

// example: put all scss in 1 file
gulp.task('concat-scss', () => {
	return gulp.src(testFiles)
		.pipe(concat('style.scss'))
		.pipe(gulp.dest(outputDir));
});

var watch = gulp.task('watch', () => {
	return gulp.watch(testFiles, ['concat-scss']);
})

gulp.task('default', gulp.parallel('concat-scss', 'watch'));