from services.refresh_data import handle_refresh


def lambda_handler(event, context):
    handle_refresh()


if __name__ == '__main__':
    handle_refresh()
