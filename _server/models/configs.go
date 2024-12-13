package models

type Configs struct {
	ID         uint   `gorm:"primaryKey"`
	ConfigName string `gorm:"size:50;not null;unique"`
	Value      string `gorm:"size:200;default:''"`
}
