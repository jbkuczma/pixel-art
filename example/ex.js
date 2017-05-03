'use strict'

// import Pixel_Art from 'pixel'
let p = require('../src/pixel')
let pixel = new p.Pixel_Art()

// pixel.loadImage('chicago_test.jpg').then((image) => {
//     pixel.saturateImage(image, 50).then((saturatedImage) => {
//         console.log('good')
//     })
// })

let savedFilePath = __dirname + '/test.png'
pixel.makePixelArt('chicago_test.png', savedFilePath)