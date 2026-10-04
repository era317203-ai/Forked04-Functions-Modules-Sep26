# main.py
# Основная программа для проверки сообщений на спам

import spam_utils as su

SPAM_WORDS = ["скидка", "бесплатно", "выигрыш", "кликни", "подпишись"]


def main():
    # Ваш код здесь
    message = input ("Введите текс")
    warnings, publish = su.moderate_message(message,SPAM_WORDS)
    for warning in warnings:
        print(warning)
    if publish:
        print(message)
    else:
        print("Сообщение не публикуется")
        
if __name__ == "__main__":
    main()
