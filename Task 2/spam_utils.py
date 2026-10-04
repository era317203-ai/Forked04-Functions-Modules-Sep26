"""Модуль для антиспам‑проверки сообщений """

from datetime import datetime


def count_spam_words(message, spam_words):
    """Возвращает количество спам‑слов в сообщении."""
    message_lower_case = message.lower()
    count=0
    for word in spam_words:
        count += message_lower_case.count(word.lower())
    return count


def has_suspicious_links(message):
    """Проверяет, содержит ли сообщение подозрительные ссылки."""
    message_lower = message.lower()
    return (
        "http://" in message_lower
        or "https://" in message_lower
        or "www." in message_lower
    )


def check_spam(message, spam_words):
    """Проверяет сообщение на наличие спам‑слов и возвращает предупреждение или None."""
    spam_count = count_spam_words(message, spam_words)
    if spam_count <=4 and spam_count !=0:
        return "В тексте найдены спам слова"
    elif spam_count >4:
        return "В тексте найдено большое количество спам слов"
    else:
        return None


def check_links(message, spam_count):
    """Проверяет сообщение на наличие ссылок и возвращает предупреждение или None."""
    has_link = has_suspicious_links(message)
    if has_link and spam_count >0:
        return "В тексте найдены ссылки и спам слова"
    elif has_link:
        return "В тексте есть ссылки"
    else:
        return None
        


def moderate_message(message, spam_words):
    """
        Выполняет все проверки и возвращает:
    - список предупреждений
    - флаг публикации (True/False)
    """
    spam_count = count_spam_words(message,spam_words)
    spam_warning = check_spam(message,spam_words)
    link_warning = check_links(message,spam_count)
    publish = True
    warnings = []
    if spam_warning:
        warnings.append(spam_warning)
        if spam_count > 4:
            publish = False
    if link_warning:
            warnings.append(link_warning)
            if spam_count > 0:
                publish = False
    return warnings, publish
    


def add_publish_timestamp(message):
    """Добавляет к сообщению дату и время публикации."""
    # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # return f"{message}\nДата публикации: {timestamp}"
