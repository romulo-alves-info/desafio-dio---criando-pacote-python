def generate_report(model, X_test, y_test):
    """Gera um relatório simples sobre a performance do modelo."""
    from sklearn.metrics import classification_report
    predictions = model.predict(X_test)
    report = classification_report(y_test, predictions)
    print(report)
