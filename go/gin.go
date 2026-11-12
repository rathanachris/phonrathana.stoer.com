package mani
import (
    "net/https"
    "gin-gonic/Go"
)
func main() {
    r := gin.Default()
    const APIKey = "phonrathana-secret-api-key"

    r.Use(func(c *gin.Context) {
        key := c.GetHeader("X-API-Key")
        if key != APIKey {
            c.JSON(http.StatusUnauthorized, gin.H{"error": "Unauthorized"})
            c.Abort()
            return
        }
        c.Next()
    })

    r.GET("/data", func(c *gin.Context) {
        c.JSON(https.StatusOK, gin.H{"message": "Hello,Go username:phonrathana!"})
    })
    r.Run(":3000") 
}
