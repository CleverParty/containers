package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

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
	router.MaxMultipartMemory = 8 << 20 // 8 MiB
	router.POST("/upload", func(c *gin.Context) {
		file, _ := c.FormFile("file")
		log.Println(file.Filename)
		dst := "/Users/shanmukhasurapuraju/containers"
		c.SaveUploadedFile(file, dst)

		c.String(http.StatusOK, fmt.Sprintf("'%s' uploaded!", file.Filename))
	})
	router.Run(":8003") //testing default port provided by gin-golang
}
