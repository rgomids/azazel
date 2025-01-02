package models

type GenerateRequest struct {
	Message string `json:"message"`
}

type GenerateResponse struct {
	Response string `json:"response"`
}

type Message struct {
	Content string `json:"content"`
}
