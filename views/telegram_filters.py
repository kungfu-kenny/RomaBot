from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Filter


class CheckTextResend(Filter):
    key = "is_basic_filter"

    async def check(self, call:CallbackQuery) -> bool:
        return len(call.data.split('_')) == 3 and call.data.split('_')[0] == '100'

class CheckHistoryNext(Filter):
    key = 'is_history_next_values'

    async def check(self, call:CallbackQuery) -> bool:
        return len(call.data.split('_')) == 4 and call.data.split('_')[0] == '101'