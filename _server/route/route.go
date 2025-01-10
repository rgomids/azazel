package route

import (
	"azazel/controller"

	"github.com/gin-gonic/gin"
)

func ServeRoutes() {
	router := gin.Default()

	router.POST("/generate", controller.HandleGeneration)
	router.GET("/services", controller.HandleServices)
	router.GET("/options", controller.HandleConfigList)
	router.PATCH("/update", controller.HandleConfigUpdate)

	router.Run("0.0.0.0:8080")
}
