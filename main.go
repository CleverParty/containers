package main

import "github.com/gin-gonic/gin"

//testing docker containerisation on golang:alpine package

func main() {
	router := gin.Default()
	router.GET("/indexVal", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "value is : %v ", // This will return a json response on /indexVal extension
		})
	})
	router.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "ping", // This will return a json response on /ping extension
		})
	})
	router.Run(":3007") //testing default port provided by gin-golang
}
