from typing import Any
from typing import Dict
from typing import List
from typing import Union
from typing import Callable
from typing import Optional
from typing import Text

from pypinyin.constants import Style


TStyle = Style
TErrors = Union[Callable[[Text], Text], Text]
TPinyinResult = List[List[Text]]
TErrorResult = Union[Text, List[Text], None]
TNoPinyinResult = Union[TPinyinResult, List[Text], Text, None]


class Converter(object):
    def convert(self, words: Text, style: TStyle, heteronym: bool,
                errors: TErrors, strict: bool = ...,
                **kwargs: Any) -> TPinyinResult: ...


class DefaultConverter(Converter):

    def convert(self, words: Text, style: TStyle, heteronym: bool,
                errors: TErrors, strict: bool = ...,
                **kwargs: Any) -> TPinyinResult: ...

    def pre_convert_style(self, han: Text, orig_pinyin: Text, style: TStyle,
                          strict: bool, **kwargs: Any) -> Optional[Text]: ...

    def convert_style(self, han: Text, orig_pinyin: Text, style: TStyle,
                      strict: bool, **kwargs: Any) -> Text: ...

    def post_convert_style(self, han: Text, orig_pinyin: Text,
                           converted_pinyin: Text, style: TStyle,
                           strict: bool, **kwargs: Any) -> Optional[Text]: ...

    def pre_handle_nopinyin(self, chars: Text, errors: TErrors,
                            heteronym: bool) -> TNoPinyinResult: ...

    def handle_nopinyin(self, chars: Text, errors: TErrors = ...,
                        heteronym: bool = ..., **kwargs: Any) -> TPinyinResult: ...

    def post_handle_nopinyin(self, chars: Text, errors: TErrors, heteronym: bool,
                             pinyin: TNoPinyinResult, **kwargs: Any) -> TNoPinyinResult: ...

    def post_pinyin(self, han: Text, heteronym: bool,
                    pinyin: TPinyinResult,
                    **kwargs: Any) -> Union[TPinyinResult, None]: ...

    def _phrase_pinyin(self, phrase: Text, style: TStyle, heteronym: bool,
                       errors: TErrors = ..., strict: bool = ...) -> TPinyinResult: ...

    def _single_pinyin(self, han: Text, style: TStyle, heteronym: bool,
                       errors: TErrors = ..., strict: bool = ...) -> TPinyinResult: ...

    def _convert_style(self, han: Text, pinyin: Text, style: TStyle,
                       strict: bool, default: Text, **kwargs: Any) -> Text: ...

    def _convert_nopinyin_chars(self, chars: Text,
                                errors: TErrors = ...) -> TNoPinyinResult: ...
