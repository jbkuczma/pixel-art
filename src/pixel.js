'use strict'

let Jimp = require('Jimp')


class Pixel_Art {

    loadImage(path) {
        return new Promise((resolve, reject) => {
            let image = Jimp.read(path)
            resolve(image)
            .catch( (error) => {
                console.error(error)
            })
        })
    }

    saturateImage(image, value) {
        return new Promise((resolve, reject) => {
            let saturatedImage = image.color([
                                    {apply: 'saturate', params: [ value ]}
                                ])
            resolve(saturatedImage)
        })
    }

    adjustBlackLevels(image, value) {

    }

    adjustWhiteLevels(image, value) {

    }

    resizeWithPixelDimension(image, size) {

    }

    resizeWithPixelPercent(image, percent) {

    }

    saveImage(image, path) {
        return new Promise((resolve, reject) => {
            image.write(path)
            resolve()
        })
    }

    makePixelArt(file, savedFilePath) {
        this.loadImage(file)
            .then( (image) => {return this.saturateImage(image, 25)})
            .then( (image) => {return this.saveImage(image, savedFilePath)})
            .then( () => {
                console.log('complete')
            }) 
    }
}


module.exports = { Pixel_Art }