package models

import (
	"errors"

	"gorm.io/gorm"
)

type Configs struct {
	ID         uint   `gorm:"primaryKey"`
	ConfigName string `gorm:"size:50;not null;unique"`
	Value      string `gorm:"size:200;default:''"`
}

func (c *Configs) UpdateConfig(db *gorm.DB) error {
	var existingConfig Configs
	if err := db.Where("config_name=?", c.ConfigName).First(&existingConfig).Error; err != nil {
		if errors.Is(err, gorm.ErrRecordNotFound) {
			return errors.New("config not found")
		}
		return err
	}

	existingConfig.Value = c.Value

	if err := db.Save(&existingConfig).Error; err != nil {
		return err
	}

	*c = existingConfig

	return nil
}

func (c *Configs) ListConfigNames(db *gorm.DB) ([]string, error) {
	var configNames []string
	if err := db.Model(&Configs{}).Pluck("config_name", &configNames).Error; err != nil {
		return nil, err
	}
	return configNames, nil
}
