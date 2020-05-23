package main

import "github.com/gin-gonic/gin"

//testing docker containerisation on golang:alpine package
//docker package alpine should have the golang packages
func main() {
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong", // This will return a json response on /ping extension
		})
	})
	r.Run(":3000") //testing defaulkt port provided by gin-golang
}
