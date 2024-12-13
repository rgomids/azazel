package route

import (
	"azazel/controller"

	"github.com/gin-gonic/gin"
)

func ServeRoutes() {
	router := gin.Default()

	router.POST("/generate", controller.ServeGenerate)
	router.GET("/info", controller.ServeInfo)
	router.PATCH("/change", controller.ServePatch)

	router.Run("0.0.0.0:8080")

}
