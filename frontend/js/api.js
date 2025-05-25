/**
 * API Service for Python Quiz Application
 * Handles all interactions with the backend API
 */

// Base URL for the API
const API_BASE_URL = 'http://localhost:8000';

// API Service object
const ApiService = {
    /**
     * Fetch all questions from the API
     * @returns {Promise<Array>} Array of questions
     */
    getAllQuestions: async function() {
        try {
            const response = await fetch(`${API_BASE_URL}/questions`);

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('Error fetching all questions:', error);
            throw error;
        }
    },

    /**
     * Fetch a specific question by ID
     * @param {number} id - Question ID
     * @returns {Promise<Object>} Question object
     */
    getQuestionById: async function(id) {
        try {
            const response = await fetch(`${API_BASE_URL}/questions/${id}`);

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error(`Error fetching question with ID ${id}:`, error);
            throw error;
        }
    },

    /**
     * Fetch a random question
     * @returns {Promise<Object>} Random question object
     */
    getRandomQuestion: async function() {
        try {
            const response = await fetch(`${API_BASE_URL}/questions/random`);

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('Error fetching random question:', error);
            throw error;
        }
    },

    /**
     * Submit an answer for a specific question
     * @param {number} questionId - Question ID
     * @param {string} answer - Selected answer (a, b, c, or d)
     * @returns {Promise<Object>} Answer response object
     */
    submitAnswer: async function(questionId, answer) {
        try {
            const response = await fetch(`${API_BASE_URL}/questions/${questionId}/answer`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ answer })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error(`Error submitting answer for question ${questionId}:`, error);
            throw error;
        }
    },

    /**
     * Quit the quiz application by sending a request to the server to terminate
     * @returns {Promise<Object>} Response from the server
     */
    quitQuiz: async function() {
        try {
            const response = await fetch(`${API_BASE_URL}/quit`, {
                method: 'POST'
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('Error quitting quiz:', error);
            // Even if there's an error, we want to close the window
            window.close();
            throw error;
        }
    }
};

// Export the API Service
window.ApiService = ApiService;
