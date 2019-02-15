var CirclesMaster = function() {
  return {
    // Circles Master v1
    initCirclesMaster: function() {
      Circles.create({
        id: 'circle-1',
        radius: 80,
        value: 84,
        maxValue: 100,
        width: 10,
        text: function(value) {
          return value;
        },
        colors: ['#f8f8f8', '#e74c3c'],
        duration: 400,
        wrpClass: 'circles-wrp',
        textClass: 'circles-text',
        valueStrokeClass: 'circles-valueStroke',
        maxValueStrokeClass: 'circles-maxValueStroke',
        styleWrapper: true,
        styleText: true
      });

      Circles.create({
        id: 'circle-2',
        radius: 80,
        value: 34,
        maxValue: 100,
        width: 10,
        text: function(value) {
          return value;
        },
        colors: ['#f8f8f8', '#e74c3c'],
        duration: 400,
        wrpClass: 'circles-wrp',
        textClass: 'circles-text',
        valueStrokeClass: 'circles-valueStroke',
        maxValueStrokeClass: 'circles-maxValueStroke',
        styleWrapper: true,
        styleText: true
      });

      Circles.create({
        id: 'circle-3',
        radius: 80,
        value: 35,
        maxValue: 100,
        width: 10,
        text: function(value) {
          return value;
        },
        colors: ['#f8f8f8', '#e74c3c'],
        duration: 400,
        wrpClass: 'circles-wrp',
        textClass: 'circles-text',
        valueStrokeClass: 'circles-valueStroke',
        maxValueStrokeClass: 'circles-maxValueStroke',
        styleWrapper: true,
        styleText: true
      });

      Circles.create({
        id: 'circle-4',
        radius: 80,
        value: 67,
        maxValue: 100,
        width: 10,
        text: function(value) {
          return value;
        },
        colors: ['#f8f8f8', '#e74c3c'],
        duration: 400,
        wrpClass: 'circles-wrp',
        textClass: 'circles-text',
        valueStrokeClass: 'circles-valueStroke',
        maxValueStrokeClass: 'circles-maxValueStroke',
        styleWrapper: true,
        styleText: true
      });
    },
  };
}();
